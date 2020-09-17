----
title: "How I Host My Side Projects"
----

My goto server stack for side projects is Digitial Ocean.
I have a dedicated web node, a monolithic server that only runs Docker and Docker Compose.
I have a dedicated Postgres server.
I have a dedicated Redis server. 

To keep my cluster secure, I use DO's firewall to prevent traffic from ever getting to my server.
I use DO's VPC so that my web node may communicate with Postgres and Redis only on a private network.
These boxes are not accessible from the outside world. 

I create a floating IP and assign it to my webserver.
I update my side project's DNS to point to my floating IP.

I use DO's snapshot feature to keep working backups of my servers. 
When I need to upgrade the resources on my server, I create a new web node, and I restore my snapshot to it.
Then I reassign my floating IP to the new node.

I store all of my source code in a GitHub repository.
I use a GitHub Action to test my projects.
I use a GitHub Action to sync server configs and SSH to the box to reboot a service if a config file changes. 
I use a GitHub Action to build a production Docker image if my tests pass. 
I store my Docker images in GitHub's Container Registry.

My web node runs over two dozen services.
Every service has a folder along with a docker-compose.yml file and any config files that are needed to launch the service.

I run a Watchtower service to poll my GitHub Registry for new image updates.
When Watchtower finds a new image, it will pull the image, stop the existing container, starts a new container using the latest image, and will run an update command to manage migrations and any one-off commands that need to run for my service.
Watchtower logs these updates to Slack, so I never have to SSH to a box to see what's going on.

I run docker-crontab to manage cronjobs that each service may need.

I run a Traefik service to manage routing traffic to each container.
Each container uses LABELs to pass hints to Traefik.

I use Chamber to manage secrets with AWS and KMS.
Each container has an entry point with a chamber binary and namespace, which loads any production environment variables that are needed for the project.
Everything is encrypted and secure by default.

I use Cloudflare as my DNS provider, CDN, and to manage static media.

If any service needs access to upload user-generated content, I store it in DO Space or AWS S3.

Everything is managed from a GitHub repository, which has no access to my AWS or KMS config.

Email is managed through...

# TODO:

Add Blue/Green deploys, which so far isn't a huge issue. 
