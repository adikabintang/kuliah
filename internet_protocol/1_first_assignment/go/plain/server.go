// important tutorial:
// https://hacked.work/blog/writing-simple-http2-server-go/
// https://www.alexedwards.net/blog/golang-response-snippets
// notes on post image:
// https://astaxie.gitbooks.io/build-web-application-with-golang/en/04.5.html
// and https://github.com/zupzup/golang-http-file-upload-download/blob/master/main.go
// push example: https://github.com/golang/blog/blob/master/content/h2push/server/main.go
package main

import (
	"encoding/json"
	"io"
	"log"
	"net/http"
	"os"
	"path"
	"text/template"
)

const apiPathPrefix string = "/api/v1"

type person struct {
	Name string `json:"name"`
	Id   string `json:"id"`
}

var bintang *person = &person{
	Name: "Adika Bintang Sulaeman",
	Id:   "728214",
}

func getJsonHandler(w http.ResponseWriter, r *http.Request) {
	j, _ := json.Marshal(bintang)
	w.Header().Set("Content-Type", "application/json")
	w.Write(j)
}

func htmlHandler(w http.ResponseWriter, r *http.Request) {
	filepath := path.Join("templates", "index.html")
	tmpl, err := template.ParseFiles(filepath)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}

	if err := tmpl.Execute(w, bintang); err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}

	if pusher, ok := w.(http.Pusher); ok {
		// push is supported
		if err := pusher.Push("/templates/app.js", nil); err != nil {
			log.Printf("Failed to push: %v", err)
		}
	}
}

func postJsonHandler(w http.ResponseWriter, r *http.Request) {
	decoder := json.NewDecoder(r.Body)
	var p person
	err := decoder.Decode(&p)
	if err != nil {
		panic(err)
	}
	log.Println(p.Name)
	w.Write([]byte("the name is " + p.Name))
}

func uploadFileHandler(w http.ResponseWriter, r *http.Request) {
	log.Println("incoming HTTP POST upload")
	const maxUploadSize = 2 * 1024 * 1024 // 8 mb
	if err := r.ParseMultipartForm(maxUploadSize); err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}

	file, handler, err := r.FormFile("uploadfile")
	defer file.Close()
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
	}

	f, err := os.OpenFile("./file/"+handler.Filename, os.O_WRONLY|os.O_CREATE, 0666)
	defer f.Close()
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
	}
	io.Copy(f, file)
	w.Write([]byte("success"))
}

func main() {
	var server http.Server
	server.Addr = ":443"

	http.Handle("/templates/", http.StripPrefix("/templates/", http.FileServer(http.Dir("templates"))))

	http.HandleFunc(apiPathPrefix+"/getjson", getJsonHandler)
	http.HandleFunc(apiPathPrefix+"/postjson", postJsonHandler)
	http.HandleFunc("/", htmlHandler)
	http.HandleFunc(apiPathPrefix+"/upload", uploadFileHandler)
	server.ListenAndServeTLS("./../data/server.pem", "./../data/server.key")
}
