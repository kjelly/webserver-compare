package controllers

import "github.com/robfig/revel"

type App struct {
	*revel.Controller
}

func (c App) Index(name string, a int, b int) revel.Result {
    sum := a + b
	return c.Render(name, sum)
}
