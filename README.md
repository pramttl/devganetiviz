# devanetiviz - A mock applicaion for ganetiviz in gwm.

The application uses Django purely for testing to allow easy access to mock data.

#### "Just give me a reason, just a lil bits enough."

Why devganetiviz? When -

* (a) you already have ganetiviz inside GWM?
* (b) you already have ganetiviz-cytoscape?


Okay so here's how it goes.

I was working with the [ganetiviz-cytoscape](https://github.com/pramttl/ganetiviz-cytoscape) which
was basically the front end component of [ganetiviz](https://github.com/pramttl/ganeti_webmgr/tree/feature/13569/ganeti_web/ganetiviz) 
an extension application I am writing for [Ganeti Web Manager](https://github.com/osuosl/ganeti_webmgr) a.k.a **GWM**.

#### The main idea behind having ganetiviz-cytoscape separately was -

* If someone wants to contribute just to the front end of ganetiviz without worrying about 
  installing gwm and running a ganeti or vagrant-ganeti cluster; he should be able to do so.

* It acts as a testing zone where you get the mock cluster data required to add any new 
  front-end feature using available data.Mock data is sufficiently large which provides a 
  more insightful look than a small virtual cluster.

So that should serve as a reason for (a)

#### ganetiviz-cytoscape was good. But it lacked something.

I wanted to add a feature that fetches separate data for each instance on the graph on clicking it.
This was easy to add to ganetiviz in GWM, as I just had to add a pattern that matches different instances to the corresponding instance json data.
The json data is dynamically fetched by a GWM-RAPI proxy view, and is different for each instance, since each instance has its own parameters.

Now to get this feature in ganetiviz-cytoscape. Firstly, its okay that I return the same json data for every instance. 
(since ganetiviz-cytoscape is about mock data and not live data.)

##### But how do I create a pattern that allows me to map serveral instances to one json file?

ganetiviz-cytoscape had a devserver which was used to run a SimpleHttpServer to serve static files in the root directory of Ganetiviz.
But this server is not sufficient to provide the kind of functionality a django devserver can along with the URLConf.

**What's the solution?**

* Lets get in django devserver to work for us?
* How?
* Lets convert ganetiviz-cytoscape into a django project.
* The result = devganetiviz = THIS REPOSITORY :)

##### More advantages

Since ganetiviz is a django app itself inside GWM. 
Having devganetiviz as a separate django project keeps things very close to the GWM ganetiviz.
(ie. The diff's between the common files is less as compared to the earlier ganetiviz-cytoscape.)

### Installation

For now the installation only requires Django >= 1.4.5

        pip install -r requirements.txt


### Running

        $ cd devganetiviz
        $ ./manage.py runserver

Visit `http://localhost:8000/` to see the ganetiviz cluster graph.
There are no models so no need to run `syncdb`. :)
All the fixure data is available in json files and you should not modify them
unless you know what you are doing, as that is how the actual ganetiviz returns live data.


### Note
devganetiviz is NOT an alternative for ganetiviz in GWM. It is a complementary project to support the ganetiviz app in GWM.

