let perguntasDiaSete = document.getElementById("perguntasDiaSete");
let respostaDiaSete = document.getElementById("respostaDiaSete");
function soma(a, b) {
  return a + b;
}
function subtracao(a, b) {
  return a - b;
}
function multiplicacao(a, b) {
  return a * b;
}
function divisao(a, b) {
  return a / b;
}
function calculadora(event) {
  event.preventDefault();
  let operacao = prompt("Digite a operação desejada (soma, subtração, multiplicação, divisão ou sair):");
  if (operacao == "sair") {
    respostaDiaSete.innerHTML = "";
    respostaDiaSete.textContent = `Até a próxima.`;
    return;
  }
  let numero1 = parseFloat(prompt("Digite o primeiro número:"));
  let numero2 = parseFloat(prompt("Digite o segundo número:"));
  let resultado;
  switch (operacao) {
    case "soma":
      resultado = soma(numero1, numero2);
      break;
    case "subtração":
      resultado = subtracao(numero1, numero2);
      break;
    case "multiplicação":
      resultado = multiplicacao(numero1, numero2);
      break;
    case "divisão":
      resultado = divisao(numero1, numero2);
      break;
    default:
      return "Operação inválida.";
  }
  respostaDiaSete.innerHTML = "";
  respostaDiaSete.textContent = `O resultado da operação ${operacao} entre ${numero1} e ${numero2} é ${resultado}.`;
}
perguntasDiaSete.addEventListener('click', calculadora);