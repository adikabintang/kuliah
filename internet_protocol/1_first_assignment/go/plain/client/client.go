package main

// https://stackoverflow.com/questions/12122159/how-to-do-a-https-request-with-bad-certificate
import (
	"crypto/tls"
	"fmt"
	"io/ioutil"
	"net/http"
)

func main() {
	tr := &http.Transport{
		TLSClientConfig: &tls.Config{InsecureSkipVerify: true},
	}
	client := &http.Client{Transport: tr}
	resp, err := client.Get("https://127.0.0.1:8000/json")
	if err != nil {
		panic(err)
	} else {
		defer resp.Body.Close()
		body, _ := ioutil.ReadAll(resp.Body)
		fmt.Println("content-type: ", resp.Header)
		fmt.Println("get: \n", (string(body)))
	}

}
