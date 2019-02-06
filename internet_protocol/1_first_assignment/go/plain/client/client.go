package main

// https://stackoverflow.com/questions/12122159/how-to-do-a-https-request-with-bad-certificate
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

func httpGetJson() {
	tr := &http.Transport{
		TLSClientConfig: &tls.Config{InsecureSkipVerify: true},
	}
	client := &http.Client{Transport: tr}
	resp, err := client.Get(hostnameDest + "/getjson")
	if err != nil {
		panic(err)
	} else {
		defer resp.Body.Close()
		body, _ := ioutil.ReadAll(resp.Body)
		//fmt.Println("content-type: ", resp.Header)
		fmt.Println("get: ", (string(body)))
	}
}

func httpPostJson() {
	var landau *person = &person{
		Name: "Michael",
		Age:  24,
	}

	thePerson, _ := json.Marshal(landau)
	tr := &http.Transport{
		TLSClientConfig: &tls.Config{InsecureSkipVerify: true},
	}
	client := &http.Client{Transport: tr}
	resp, err := client.Post(hostnameDest+"/postjson", "application/json", bytes.NewBuffer(thePerson))
	if err != nil {
		log.Fatalln(err)
	}
	body, _ := ioutil.ReadAll(resp.Body)
	log.Print("Response POST: " + string(body))
}

func httpPostUpload() {
	filepath := path.Join("files", "picture.png")
	// open the file
	picture, err := os.Open(filepath)
	defer picture.Close()
	if err != nil {
		panic(err)
	}

	// values := map[string]io.Reader{
	// 	"uploadfile": picture,
	// 	//"filename": strings.NewReader("hello world!"),
	// }

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

	// for key, val := range params {
	// 	_ = writer.WriteField(key, val)
	// }
	err = writer.Close()
	if err != nil {
		panic(err)
	}

	request, _ := http.NewRequest("POST", hostnameDest+"/upload", body)
	request.Header.Add("Content-Type", writer.FormDataContentType())
	tr := &http.Transport{
		TLSClientConfig: &tls.Config{InsecureSkipVerify: true},
	}
	client := &http.Client{Transport: tr}
	resp, err := client.Do(request)
	if err != nil {
		panic(err)
	}

	log.Println(resp.Header)
	log.Println(resp.StatusCode)
	defer resp.Body.Close()
	responseBody, _ := ioutil.ReadAll(resp.Body)
	//fmt.Println("content-type: ", resp.Header)
	log.Println("get: ", (string(responseBody)))
}

func main() {
	//httpGetJson()
	//httpPostJson()
	httpPostUpload()
}
