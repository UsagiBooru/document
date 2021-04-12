# document
Project future, Install guide, OpenAPI doc belongs here.

## What is UsagiBooru?
This project try to beat current booru service and pixiv.
In other words, we aim to be an illustration posting site that is used by many people.
Currently there is only one developer, but we are looking for developers.

### Features
#### Customizable
This project uses a microservices architecture.
You can add forum service if you need a bulletin board on your site.
Also you can add wiki service if you need a wiki.
It can be customized as needed.

#### Federated
Wouldn't you like a site where you can only post derivative works of a particular anime?
This project aims to be a decentralized illustration posting site.
With federated system, you can publish to many instances only post 1 instance.
Ex. personal instance, specific anime instance, miscellaneous things instance.
This project bases ActivityPub like used in Mastodon.
And it can also work with existing instances such as Mastodon and Misskey.

#### IPFS backend
Want to keep your files permanently or reduce server load?
For that purpose, it supports IPFS, which is a distributed file system.
Of course, the conventional general delivery method can also be used.

### Architecture
#### Microservices architecture
To enable scaleable and sustainable development,
Design the repository separately according to the program interests.
The front end and back end were developed completely separately.
It is also possible to use only the back side.

#### Uses OpenAPIv3
To make the unified standard and final form concrete,
I prepared a document using OpenAPIv3.
We aim for something that works as per this document.
By adopting OpenAPI, API client development will be smooth.

#### Uses golang
The Python I've been using for a long time was easy to write, but very slow.
I chose the Go language because I am convinced that Go will be adopted in the future.


### Q&A
#### I saw you made similar project(NuxtImageBoard)
NuxtImageBoard is an OSS version of I previously created, and there are no plans to actively develop it.
This is a project that extends and rewrites it. The design is similar to before, but not compatible.

#### What is the origin of the name?
If you look at my icon and it comes to you, that's it.

#### Why AGPL?
This is because we want to ensure the transparency of the instances that are being operated.
Also, Mastodon, Misskey which I refer to, are AGPL and I wanted to follow them.