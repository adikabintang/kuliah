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
	"strconv"
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
	log.Printf("request: %s", r.Proto)
	j, _ := json.Marshal(bintang)
	w.Header().Set("Content-Type", "application/json")
	w.Write(j)
}

func uploadPageHandler(w http.ResponseWriter, r *http.Request) {
	log.Printf("request: %s", r.Proto)
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
		if err := pusher.Push("/templates/app.js", nil); err != nil {
			log.Printf("Failed to push: %v", err)
		}
	}
}

func testingSimplestHandler(w http.ResponseWriter, r *http.Request) {
	log.Printf("request: %s", r.Proto)
	log.Println("request to testingSimplest: html + simple css")
	filepath := path.Join("templates", "simplest", "testing_simplest.html")
	tmpl, err := template.ParseFiles(filepath)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}

	if err := tmpl.Execute(w, nil); err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}

	if pusher, ok := w.(http.Pusher); ok {
		if err := pusher.Push("/templates/simplest/testing.css", nil); err != nil {
			log.Printf("Failed to push: %v", err)
		}
	}
}

func simpleHandler(w http.ResponseWriter, r *http.Request) {
	log.Printf("request: %s", r.Proto)
	log.Println("request to simple: html + simple css + bootstrap + image")
	filepath := path.Join("templates", "simple", "simple.html")

	type Img struct {
		Title string
	}

	const nImages int = 30
	var d [nImages]Img
	for i := 1; i <= nImages; i++ {
		d[i-1] = Img{Title: strconv.Itoa(i)}
	}

	log.Println("pushing...")
	if pusher, ok := w.(http.Pusher); ok {
		log.Println("push is supported")

		if err := pusher.Push("/templates/simple/bootstrap/bootstrap.min.css", nil); err != nil {
			log.Printf("Failed to push: %v", err)
		}

		if err := pusher.Push("/templates/simple/simple.css", nil); err != nil {
			log.Printf("Failed to push: %v", err)
		}

		for i := 1; i <= nImages; i++ {
			if err := pusher.Push("/templates/simple/img/"+strconv.Itoa(i)+".jpeg", nil); err != nil {
				log.Printf("Failed to push: %v", err)
			}
		}
	} else {
		log.Println("push is not supported")
	}

	type D struct {
		Imgs [nImages]Img
	}
	data := D{
		Imgs: d,
	}

	tmpl, err := template.ParseFiles(filepath)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}

	if err := tmpl.Execute(w, data); err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
}

func postJsonHandler(w http.ResponseWriter, r *http.Request) {
	log.Printf("request: %s", r.Proto)
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
	log.Printf("request: %s", r.Proto)
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
	http.HandleFunc("/upload_page", uploadPageHandler)
	http.HandleFunc("/testing/simplest", testingSimplestHandler)
	http.HandleFunc("/testing/simple", simpleHandler)
	http.HandleFunc(apiPathPrefix+"/upload", uploadFileHandler)
	server.ListenAndServeTLS("./server.pem", "./server.key")
}
