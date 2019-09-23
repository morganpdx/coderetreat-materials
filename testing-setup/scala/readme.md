
## How to start testing in Scala

Scala runs on the JVM, so it requires a JDK. Of course, it also requires a Scala SDK. Setup with Maven isn't _easy_, but once done (this example aims to do this work for you), it should work with Maven commands through a terminal, through JetBrains IntelliJ IDEA (even the Community Edition), Eclipse, or other such tools or IDEs.

1. (Optional) Make a copy of this module, disconnect from the coderetreat remote, or redirect your upstream tracking to your own remote.
1. Install a Scala SDK. The Maven project file (`pom.xml`) provided here was written for Scala 2.11.12. Note: If you install a different version of Scala, some dependencies and plugins may need to have different versions specified to be compatible. Also, make sure to correct the version specified near the top of the POM.
1. Install a JDK. This project is written with Java 11 specified. Note: If you install a different version of Java, some dependencies and plugins may need to have different versions specified to be compatible (though this is less likely than with a change to the Scala version). Also, make sure to correct the version specified near the top of the POM.
1. Install Maven. This example project was built and tested with Maven 3.6.1. You may need to restart your terminal session for `mvn` to be seen on the `PATH`.
1. Navigate in your terminal to the root directory of this module before the next steps.
1. Run `mvn compile` to ensure proper setup.
1. Run `mvn test` to run all tests.
1. (Optional) Change the example test in `MySpec` so that it will fail, then run `mvn test` again to see how it reports test failures.
