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

type person struct {
	Name string `json:"name"`
	Age  int    `json:"age"`
}

func getJsonHandler(w http.ResponseWriter, r *http.Request) {
	var bintang *person = &person{
		Name: "Bintang",
		Age:  24,
	}

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

	var bintang *person = &person{
		Name: "Bintang",
		Age:  24,
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
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
	}
	defer file.Close()
	f, err := os.OpenFile("./file/"+handler.Filename, os.O_WRONLY|os.O_CREATE, 0666)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
	}
	defer f.Close()
	io.Copy(f, file)
	w.Write([]byte("success"))
}

func main() {
	var server http.Server
	server.Addr = ":8000"

	http.Handle("/templates/", http.StripPrefix("/templates/", http.FileServer(http.Dir("templates"))))

	http.HandleFunc("/getjson", getJsonHandler)
	http.HandleFunc("/postjson", postJsonHandler)
	http.HandleFunc("/static", htmlHandler)
	http.HandleFunc("/upload", uploadFileHandler)
	server.ListenAndServeTLS("./../data/server.pem", "./../data/server.key")
}
