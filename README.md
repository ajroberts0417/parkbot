# parkbot
Parkbot -- a CLI for parking spots

## Installation & Usage
1. Clone the source
`git clone git@github.com:ajroberts0417/parkbot.git`

2. Navigate into the project directory
`cd parkbot`

3. Use the CLI

#### Get help
`$ python parkbot -h`

#### Query for all the parking spots in California
```
$ python parkbot data.json --locate CA

['Church of 8 Wheels', 'Sweetgreen', 'Sandwiches n More', 'AirGarage HQ', 'Walgreens', 'The Salon', 'Archer Salon']
```

#### Query for all the parking spots in AZ, with hourly rates <= $5.00, but > $1.00
```
$ python parkbot data.json -l AZ -lte 500 -gt 100

['Tempe Beach Park', 'Safeway']
```

#### Get all lots, with no query parameters
`$ python parkbot data.json`

##### NOTE: If you're on macOS, or have python installed, this should use your native version of python.
##### If you find it doesn't work, [install python 3](https://www.codecademy.com/articles/install-python3)

## Commands
- `--locate`, `-l`: This option will query for spots by location (state only). Example: -l AZ will return spots in Arizona

- `--find_price_hourly_lte`, `-lte`. This option will query for spots where the hourly price is less than or equal to the query price. (Note: the price is in cents). Example: -lte 200 will return spots that are less than or equal to $2 per hour.

- `--find_price_hourly_gt`, `-gt`. This option will query for spots where the price is greater than the query price. (Note: the price is in cents). Example: -gt 200 will return spots that are greater than $2 per hour.

You can mix and match commands as you like to construct more complex queries!

## Contributing
1. Fork the repo
`git clone git@github.com:<YOUR_USER_NAME>/parkbot.git`

2. Navigate into your new project directory
`cd parkbot`

3. Add the source repository as a remote
`git remote add upstream git@github.com:ajroberts0417/parkbot.git`

4. Verify your remotes
(Should look something like this)
```
$ git remote -v
> origin    https://github.com/YOUR_USERNAME/parkbot.git (fetch)
> origin    https://github.com/YOUR_USERNAME/parkbot.git (push)
> upstream  https://github.com/ajroberts0417/parkbot.git (fetch)
> upstream  https://github.com/ajroberts0417/parkbot.git (push)
```

## Dependencies
- A version of python 3 installed and added to your PATH

## Testing

Testing will be added in v2! For now, I should get home from work :)

