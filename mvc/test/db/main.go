package main

import (
	db "./database"
	"./router"
)

func main() {
	defer db.SqlDB.Close()
	router := router.initRouter()
	router.Run(":8000")
}
