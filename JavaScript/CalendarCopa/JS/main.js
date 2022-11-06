let delay = -0.4;
function createCard(date, day, games){
  delay = delay + 0.4;
  return `
  <div class="card" style="animation-delay: ${delay}s">
    <h2>${date} <span>${day}</span></h2>
      <ul>
        ${games}  
      </ul>
  </div>`
}
function createGame(player1, hour, player2){
  return `
    <li>
      <img src="./Assets/icon-${player1}.svg" alt="Logo ${player1}">
      <strong>${hour}</strong>
      <img src="./Assets/icon-${player2}.svg" alt="Logo ${player2}">
    </li>
  `
}
document.querySelector("#cards").innerHTML = 
  
    createCard("24/11", "Quinta", createGame("brazil", "16:00", "serbia")) +
    
    createCard("28/11", "Segunda", 
    createGame("brazil", "13:00", "switzerland")+
    createGame("portugal", "16:00", "uruguay")) +
    
    createCard("02/12", "Sexta", createGame("cameroon", "16:00", "brazil"))    
  
