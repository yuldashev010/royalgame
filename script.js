
let coins = Number(localStorage.getItem("royalCoins")) || 5;

function updateCoins() {
    document.getElementById("coins").innerText = coins;
    localStorage.setItem("royalCoins", coins);
}

function dailyBonus() {
    let today = new Date().toDateString();
    let lastBonus = localStorage.getItem("lastBonus");

    if (lastBonus === today) {
        alert("Bugungi bonusni olib bo‘ldingiz!");
        return;
    }

    coins += 2;
    localStorage.setItem("lastBonus", today);
    updateCoins();

    alert("🎁 +2 R Coin!");
}

function game(name) {
    alert(name + " onlayn o‘yini tez orada!");
}

function page(name) {
    alert(name + " bo‘limi tez orada!");
}

updateCoins();
