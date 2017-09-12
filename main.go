package main

//import "github.com/gin-gonic/gin"

import(
	"fmt"
	"github.com/gin-gonic/gin"
	"net/http"
)

//中间件
func Middleware(c *gin.Context) {
    fmt.Println("this is a middleware!")
}


func main() {
    r := gin.Default()

    //添加中间件
    r.Use(Middleware)
    r.GET("/ping", func(c *gin.Context) {
        c.JSON(200, gin.H{
            "message": "pong",
        })
    })

    r.GET("/user/:name", func(c *gin.Context) {
        name := c.Param("name")
        c.String(http.StatusOK, "Hello %s", name)
    })
    r.Run()
}
