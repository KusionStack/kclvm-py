schema Person:
    firstName: str = "John"
    lastName: str
    @err_deprecated(version="1.16", reason="use firstName and lastName instead", strict=False)
    name: str

JohnDoe = Person {
    name: "deprecated"
}
