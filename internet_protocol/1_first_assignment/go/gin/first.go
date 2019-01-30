// example: https://github.com/gin-gonic/gin/tree/master/examples/http2
package main

import (
	"log"
	"os"

	"github.com/gin-gonic/gin"
)

func main() {
	logger := log.New(os.Stderr, "", 0)
	logger.Println("[WARNING] DON'T USE THE EMBED CERTS FROM THIS EXAMPLE IN PRODUCTION ENVIRONMENT, GENERATE YOUR OWN!")

	r := gin.Default()

	r.GET("/", func(c *gin.Context) {
		c.JSON(200, gin.H{
			"message": "pong",
		})
	})

	// Listen and Server in https://127.0.0.1:8000
	r.RunTLS(":8000", "./data/server.pem", "./data/server.key")
}
