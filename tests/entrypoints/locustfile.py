from locust import HttpUser, task


class CreateShortUrl(HttpUser):
    @task
    def create_short_urls(self):
        self.client.post("/url", json={"original_url": "https://linkedin.com", "created_by": "Shako"})
