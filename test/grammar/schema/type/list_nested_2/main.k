schema Person:
    labels: [{str:}]

alice = Person {
    "labels": [
        {
            "skin": "yellow",
            "height": 100,
            "female": True,
            "family": {"father": "John"},
            "teacher": ["Finch", "Root", "Shaw"]
        }
    ]
}
