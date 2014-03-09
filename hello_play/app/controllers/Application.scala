package controllers

import play.api._
import play.api.mvc._
import play.api.data._
import play.api.data.Forms._


object Application extends Controller {

  def index = Action { implicit request => {
    val loginForm = Form(
      tuple(
        "name" -> text,
        "a" -> number,
        "b" -> number
      )
    )
    val (name, a, b) = loginForm.bindFromRequest.get
      Ok(views.html.index(name, a + b))
    }
  }

}