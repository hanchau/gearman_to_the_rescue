### Distributed logs processor with gearman

1. Setup gearadmin and gearman with.

  `brew install gearmand` or

  `apt install gearman-job-server`

2. Setup gearman job server for mac.

   [follow the instructions](https://www.richardsumilang.com/server/gearman/install-gearman-on-os-x/)

3. You can get the gearman python package from

   [gearman package](https://www.github.com/hanchau/log_processor/dependencies/gearman)


4. I'm using python

  ```
    $ source /path/to/env
    $ python -m site
    $ cp -r <path/to/gearman/package/dir> </path/to/env>/lib/python3.8/site-packages/
    $ pip install -r requirements.txt
  ```

5. To check the proper installation do

  ```
    $ gearadmin --server-version
    $ gearadmin --status
  ```
6. To check the proper installation of the python gearman package do
  ```
    $ python -c "import gearman"
  ```
  if no error is thrown then you are good to go.
