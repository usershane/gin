package main

//import "github.com/gin-gonic/gin"

import(
	"fmt"
	"github.com/gin-gonic/gin"
	//	"github.com/gin-gonic/gin/binding"
	"net/http"
)

//实现表单数据绑定
type LoginForm struct {
    User     string `form:"user"     binding:"required"`
    Password string `form:"password" binding:"required"`
}

//中间件
func Middleware(c *gin.Context) {
	fmt.Println("this is a middleware!")
}

// 路由组的中间件
func GroupMidd(c *gin.Context) {
        fmt.Println("Group middleware!")
}


// 路由组的测试
func HelloGroupA( c *gin.Context ){
	c.String(http.StatusOK, "Hello Group-a")
}

// 路由组的测试
func HelloGroupB( c *gin.Context ){
	c.String(http.StatusOK, "Hello Group-b")
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

	// 路由参数的使用
	r.GET("/user/:name", func(c *gin.Context) {
		name := c.Param("name")
		c.String(http.StatusOK, "Hello %s", name)
	})

	// 路由参数的使用
	r.GET("/user/:name/*action", func(c *gin.Context) {
		name := c.Param("name")
		action := c.Param("action")
		message := name + " is " + action
		c.String(http.StatusOK, message)
	})

	// 路由组
	ra := r.Group("/group-a")
	ra.Use( GroupMidd )
	ra.GET("/hello", HelloGroupA )

	rb := r.Group("/group-b")
	rb.GET("/world", HelloGroupB)


	r.StaticFS("/show", http.Dir("."))
	r.StaticFile("/image", "./static/image/image01.jpg")

	// 使用模板
	r.LoadHTMLGlob("mvc/view/*")
	r.GET( "/index", func(c *gin.Context){
		c.HTML(http.StatusOK, "index.tmpl", gin.H{
			"title": "GIN: 测试加载HTML模板",
		})
	})

	// 下面测试重定向
	r.GET("/redirect", func(c *gin.Context) {
		c.Redirect(http.StatusMovedPermanently, "www.baidu.com")
	})

	// 表单数据绑定
	r.POST("/login", func(c *gin.Context) {
        // you can bind multipart form with explicit binding declaration:
        // c.BindWith(&form, binding.Form)
        // or you can simply use autobinding with Bind method:
		var form LoginForm
		// in this case proper binding will be automatically selected
		if c.Bind(&form) == nil {
			if form.User == "user" && form.Password == "password" {
				c.JSON(200, gin.H{"status": "you are logged in"})
			} else {
				c.JSON(401, gin.H{"status": "unauthorized"})
			}
		}
	})

	r.Run()
}
