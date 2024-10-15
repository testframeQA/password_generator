const crypto = require("crypto");
const process = require("process");

function generatePassword(length, digits) {
  if (digits > length) {
    throw new Error(
      "Number of digits cannot exceed the total password length.",
    );
  }

  const lettersLength = length - digits;
  const letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";
  const numbers = "0123456789";

  let passwordLetters = "";
  for (let i = 0; i < lettersLength; i++) {
    const randomIndex = crypto.randomInt(0, letters.length);
    passwordLetters += letters[randomIndex];
  }

  let passwordDigits = "";
  for (let i = 0; i < digits; i++) {
    const randomIndex = crypto.randomInt(0, numbers.length);
    passwordDigits += numbers[randomIndex];
  }

  let passwordArray = (passwordLetters + passwordDigits).split("");
  for (let i = passwordArray.length - 1; i > 0; i--) {
    const j = crypto.randomInt(0, i + 1);
    [passwordArray[i], passwordArray[j]] = [passwordArray[j], passwordArray[i]];
  }

  const password = passwordArray.join("");

  console.log(
    `${length}-character password with ${digits} digits: ${password}`,
  );
}

const args = process.argv.slice(2);
if (args.length !== 2) {
  console.log("Usage: node password_generator.js <length> <digits>");
  process.exit(1);
}

const length = parseInt(args[0], 10);
const digits = parseInt(args[1], 10);

generatePassword(length, digits);
