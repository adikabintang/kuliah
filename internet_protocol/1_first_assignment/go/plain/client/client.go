package main

// https://stackoverflow.com/questions/12122159/how-to-do-a-https-request-with-bad-certificate
// good example: https://gist.github.com/mattetti/5914158/f4d1393d83ebedc682a3c8e7bdc6b49670083b84
import (
	"bytes"
	"crypto/tls"
	"encoding/json"
	"fmt"
	"io/ioutil"
	"log"
	"mime/multipart"
	"net/http"
	"os"
	"path"
)

const hostnameDest string = "https://127.0.0.1:8000"

type person struct {
	Name string `json:"name"`
	Age  int    `json:"age"`
}

/*
wait and read response
wait until connection finishes
making sure using the same connection for the next request
*/
func printResponse(resp *http.Response) {
	defer resp.Body.Close()
	responseBody, _ := ioutil.ReadAll(resp.Body)
	log.Println(resp.Header)
	log.Println(resp.StatusCode)
	log.Println("get: ", (string(responseBody)))
}

func httpGetJson(client http.Client) {
	resp, err := client.Get(hostnameDest + "/getjson")
	if err != nil {
		panic(err)
	} else {
		defer resp.Body.Close()
		body, _ := ioutil.ReadAll(resp.Body)
		fmt.Println("get: ", (string(body)))
	}

	printResponse(resp)
}

func httpPostJson(client http.Client) {
	var landau *person = &person{
		Name: "Michael",
		Age:  24,
	}

	thePerson, _ := json.Marshal(landau)
	resp, err := client.Post(hostnameDest+"/postjson", "application/json", bytes.NewBuffer(thePerson))
	if err != nil {
		log.Fatalln(err)
	}

	printResponse(resp)
}

func httpPostUpload(client http.Client) {
	filepath := path.Join("files", "picture.png")
	picture, err := os.Open(filepath)
	defer picture.Close()
	if err != nil {
		panic(err)
	}

	pictureContent, err := ioutil.ReadAll(picture)
	if err != nil {
		panic(err)
	}

	fi, err := picture.Stat()
	if err != nil {
		panic(err)
	}

	body := new(bytes.Buffer)
	writer := multipart.NewWriter(body)
	part, err := writer.CreateFormFile("uploadfile", fi.Name())
	if err != nil {
		panic(err)
	}
	part.Write(pictureContent)

	err = writer.Close()
	if err != nil {
		panic(err)
	}

	request, _ := http.NewRequest("POST", hostnameDest+"/upload", body)
	request.Header.Add("Content-Type", writer.FormDataContentType())
	resp, err := client.Do(request)
	if err != nil {
		panic(err)
	}

	printResponse(resp)
}

func main() {
	tr := &http.Transport{
		TLSClientConfig: &tls.Config{InsecureSkipVerify: true},
	}
	client := &http.Client{Transport: tr}

	//httpGetJson(*client)
	httpPostJson(*client)
	//httpPostUpload(*client)
}
