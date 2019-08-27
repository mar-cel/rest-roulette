
<img src="https://www.roulette.rip/static/assets/img/background/bg.jpg" />

# REST Roulette

<b>Play your luck in roulette.</b>

Free, open-source JSON REST API

<b>[www.roulette.rip](https://www.roulette.rip)</b>
</center>

## Usage
<b>Base URL:</b>
<pre>https://www.roulette.rip</pre>
<br>

### Play game
<pre><b>GET</b> /api/play</pre>

<b>Required parameters:</b>
- `bet`: odd, even, low, high, red, black, green, or [0 through 36]
- `wager`: any number

## Example
<b>Request:</b>
<pre> <b>GET</b> /api/play?bet=low&wager=200</pre>
<b>Response:</b>
```json
{
  "bet": {
    "bet": "low", 
    "payout": "400.00", 
    "payout_rate": 1, 
    "wager": "200.00", 
    "win": true
  }, 
  "roll": {
    "color": "red", 
    "number": 1, 
    "parity": "odd"
  }, 
  "success": true
}
```

## Gameplay
Roulette is a common casino game where players can place bets on either a single number, various groupings of numbers, the colors red or black, whether the number is odd or even, or if the numbers are high (19–36) or low (1–18).

[More Information](https://en.wikipedia.org/wiki/Roulette)

## Bets and Payouts
This API supports the following bets:
- <b>Odd/Even:</b> 1 to 1
- <b>Low/High:</b> 1 to 1
- <b>Red/Black:</b> 1 to 1
- <b>Green:</b> 35 to 1
- <b>Number:</b> 36 to 1


## Development
Version <b>1.0.0</b>

Written by <b>Marcel Perez</b>

Uses <b>Flask</b> for <b>Python</b>

Roulette photo by <b>Pixabay</b>