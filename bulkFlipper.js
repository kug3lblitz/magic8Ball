function flipCoin() {
  return Math.random() < 0.5 ? "heads" : "tails";
}

function flipCoin1000() {
  let heads = 0;
  let tails = 0;
  for (let i = 0; i < 1000; i++) {
    if (flipCoin() === "heads") {
      heads++;
    } else {
      tails++;
    }
  }
  return { heads, tails };
}

const results = flipCoin1000();
console.log(results); // { heads: 503, tails: 497 }
