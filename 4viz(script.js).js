async function generatePassword() {
    const length = document.getElementById('length').value;
    const useSymbols = document.getElementById('symbols').checked;
    const useDigits = document.getElementById('digits').checked;
    
    const response = await fetch(`/generate?length=${length}&use_symbols=${useSymbols}&use_digits=${useDigits}`);
    const data = await response.json();
    
    document.getElementById('password').value = data.password;
    updateStrengthIndicator(data.strength);
}

function updateStrengthIndicator(strength) {
    const indicator = document.getElementById('strength');
    indicator.style.width = `${strength * 10}%`;
    indicator.style.background = strength > 7 ? '#4CAF50' : strength > 4 ? '#FFC107' : '#F44336';
}

function copyPassword() {
    const passwordField = document.getElementById('password');
    passwordField.select();
    document.execCommand('copy');
    alert('Пароль скопирован!');
}