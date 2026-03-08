// Инициализация баланса
let balance = parseInt(localStorage.getItem("balance")||"1000");
document.getElementById("balance")?.innerText = balance;

// Переходы
function goToCase(page){ window.location.href=page; }
function openProfile(){ window.location.href="profile.html"; }
function openAdmin(){
    const currentUser = "@ceotinkov"; // Юзер админа
    if(currentUser!="@ceotinkov"){ alert("Нет доступа!"); return; }
    window.location.href="admin.html";
}
function goBack(){ window.history.back(); }

// Покупка кейса
function buyCase(price){
    if(balance < price){
        alert("Недостаточно монет 🪙");
        return; // не покупаем
    }
    balance -= price;
    localStorage.setItem("balance", balance);
    document.getElementById("balance").innerText = balance;
    document.getElementById("buyCaseBtn").style.display = "none";
    document.getElementById("openCaseBtn").style.display = "inline-block";
}

// Открытие кейса с анимацией
function openLoot(){
    // Случайная награда
    const loot = Math.floor(Math.random()*500 + 50); 
    balance += loot;
    localStorage.setItem("balance", balance);
    document.getElementById("balance").innerText = balance;

    // Анимация выпадения монет и звезд
    const lootAnim = document.getElementById("lootAnim");
    lootAnim.innerHTML = ""; // очистка

    for(let i=0;i<15;i++){
        // Монетки
        const coin = document.createElement("div");
        coin.className="coin-anim";
        coin.style.left = Math.random()*80 + "%";
        coin.innerText="🪙";
        lootAnim.appendChild(coin);

        // Звезды
        const star = document.createElement("div");
        star.className="coin-anim";
        star.style.left = Math.random()*80 + "%";
        star.innerText="⭐";
        lootAnim.appendChild(star);

        setTimeout(()=>{coin.remove(); star.remove();}, 2000);
    }

    // Сообщение о выигрыше
    setTimeout(()=>{ alert(`Вы выиграли ${loot} 🪙`); }, 500);
}