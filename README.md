# covid-19

Scraping covid-19 data from [worldometers.info](worldometers.info)

## Info

### Goal

This repo is made for scraping data of covid-19 from [worldometers](https://www.worldometers.info/coronavirus), and is public for everone to look and work apon.

### Data Viewing

This code stores data from [worldometers.info](https://www.worldometers.info/coronavirus) into the `data` directory of this repo. It stores a json and a csv format of the data with the file name formate being `data-D-M-Y.FORMATE` where `D` stands for day, `M` stands for mounth, `Y` stands for year and `FORMATE` standing for the formate of the file e.g. `json` or `csv`. If you want to view the data from [Github](https://github.com/bin0x00/Corona/tree/master/data) itself I recoment you to view the csv format as the webiste will format it into a clean table.

### What does this code do

It does two things:
* It will scrap all the important(the table) from [worldometers](https://www.worldometers.info/coronavirus) everday 10 minutes before midnight. Thanks to [Github Actions](https://github.com/features/actions).
* It can scrap data from the last snapshots of the all the days it has been snapshoted from the [Way Back Machine](https://web.archive.org/web/*/https://www.worldometers.info/coronavirus/) and store it.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the requirements.

```bash
python3 -m pip install -r requirements.txt
```

## Usage

Run the yesterdays scrap locally:

```bash
python3 Scrap.py
```

Scrap all dates data from [worldometers](https://www.worldometers.info/coronavirus) over WayBackMachine:
> ***Note***: *An `scrap_error.txt` file will be created if not already created and will append the error file with the  `raw_url` which can be used incase of an `1040 Database Error` from WayBackMachine when Scrap_wayback.py file is ran*

```bash
python3 Scrap_wayback.py
```

Scrap data from a particular `date` over WayBackMachine:

```bash
python3 Scrap_wayback.py [<--date>|<-d>] <last-snapshot|first-snapshot> <date-like-29-01-2020>
```

Scrap data from a particular `raw_url` over WayBackMachine:

```bash
python3 Scrap_wayback.py [<--raw-url>|<-r>] <raw_url>
```

## TODO

* Work apon making more usable code
    * Make `Scrap_wayback.py` use multiprocess for faster processing
    * Make a cleaner python application to clean the data from `statistics/curve/get_data.py`
    * Make better way of extracting `argv`(s)
* Make a pipy library from it
    * Make a proper doc of how to use the lib
* Work on better README
* List it on others repos
