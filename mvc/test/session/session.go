package main

import (
	"github.com/gin-gonic/contrib/sessions"
	"github.com/gin-gonic/gin"
)

func main() {
	r := gin.Default()
	store := sessions.NewCookieStore([]byte("secret"))
	r.Use(sessions.Sessions("mysession", store))

	r.GET("/incr", func(c *gin.Context) {
		session := sessions.Default(c)
		var count int
		v := session.Get("count")
		if v == nil {
			count = 0
		} else {
			count = v.(int)
			count += 1
		}
		session.Set("count", count)
		session.Save()
		c.JSON(200, gin.H{"count": count})
	})

	r.GET("/set/:name", func( c *gin.Context ){
		session := sessions.Default(c)
		session.Set( "name", c.Param("name") )
		session.Save()
		c.JSON(200, gin.H{"name": "success" })
	})

	r.GET("/get", func( c *gin.Context ){
		session := sessions.Default(c)
		name := session.Get("name")
		c.JSON(200, gin.H{"name": name })
	})


	r.Run(":8000")
}
