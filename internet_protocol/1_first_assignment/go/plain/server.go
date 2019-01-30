// important tutorial:
// https://hacked.work/blog/writing-simple-http2-server-go/
// https://www.alexedwards.net/blog/golang-response-snippets
package main

import (
	"encoding/json"
	"net/http"
	"path"
	"text/template"
)

type person struct {
	Name string `json:"name"`
	Age  int    `json:"age"`
}

var bintang *person = &person{
	Name: "Bintang",
	Age:  28,
}

func jsonHandler(w http.ResponseWriter, r *http.Request) {
	j, _ := json.Marshal(bintang)
	w.Header().Set("Content-Type", "application/json")
	w.Write(j)
}

func htmlHandler(w http.ResponseWriter, r *http.Request) {
	fp := path.Join("templates", "index.html")
	tmpl, err := template.ParseFiles(fp)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}

	if err := tmpl.Execute(w, bintang); err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
	}
}

func main() {
	var server http.Server
	server.Addr = ":8000"

	http.HandleFunc("/json", jsonHandler)
	http.HandleFunc("/static", htmlHandler)
	server.ListenAndServeTLS("./../data/server.pem", "./../data/server.key")
}
