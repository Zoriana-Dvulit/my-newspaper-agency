from newspaper.models import Topic, Redactor, Newspaper


def create_user_objects():
    topic1 = Topic.objects.create(name="Politics")
    topic2 = Topic.objects.create(name="Entertainment")

    redactor1 = Redactor.objects.create(username="john", first_name="John", last_name="Doe", email="john@example.com",
                                        years_of_experience=5)
    redactor2 = Redactor.objects.create(username="jane", first_name="Jane", last_name="Doe", email="jane@example.com",
                                        years_of_experience=3)

    newspaper1 = Newspaper.objects.create(title="Trump wins election", content="...", published_date=timezone.now(),
                                          topic=topic1)
    newspaper2 = Newspaper.objects.create(title="New movie released", content="...", published_date=timezone.now(),
                                          topic=topic2)

    newspaper1.publishers.add(redactor1)
    newspaper2.publishers.add(redactor2)
