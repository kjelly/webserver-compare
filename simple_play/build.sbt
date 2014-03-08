name := "simple_play"

version := "1.0-SNAPSHOT"

libraryDependencies ++= Seq(
  jdbc,
  anorm,
  cache
)

libraryDependencies += "ch.qos.logback" % "logback-classic" % "1.0.1"

play.Project.playScalaSettings
