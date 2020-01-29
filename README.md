# parkbot
Parkbot -- a CLI for parking spots

## Installation & Usage
1. Clone the source
`git clone git@github.com:ajroberts0417/parkbot.git`

2. Navigate into the project directory
`cd parkbot`

3. Use the CLI
```
$ python parkbot.py data.json locate AZ

> Church A, Church C, ...
```

```
$ python parkbot.py data.json find_price_hourly_lte 200

> Church B, Hotel E, ...
```

##### NOTE: If you're on macOS, or have python installed, this should use your native version of python.
##### If you find it doesn't work, [install python 3](https://www.codecademy.com/articles/install-python3)

## Commands
- `locate`: This command will return a list of spot names by location (state only). Example: locate AZ will return spots in Arizona

- `find_price_hourly_lte`. This command will return a list of spot names where the hourly price is less than or equal to the query price. (Note: the price is in cents). Example: find_price_hourly_lte 200 should return spots that are less than or equal to $2 per hour.

- `find_price_hourly_gt`. This command will return a list of spot names where the price is greater than the query price. (Note: the price is in cents). Example: find_price_hourly_gt 200 will return spots that are greater than $2.00 per hour.

Example ou

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


