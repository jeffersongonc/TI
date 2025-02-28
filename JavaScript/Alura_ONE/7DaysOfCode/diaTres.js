let perguntasDiaTres = document.getElementById('perguntasDiaTres');

function fluxoDecisao(event){
    event.preventDefault();
    let perguntaUm;
    let perguntaDois;
    let perguntaTres;
    let perguntaQuatro;
    let respostaDiaTres = document.getElementById("respostaDiaTres");

    perguntaUm = perguntaArea();
    perguntaDois = perguntaLinguagem(perguntaUm);
    perguntaTres = perguntaDesejo();
    perguntaQuatro = perguntaNovasTecnologias();

    respostaDiaTres.innerHTML = `Suas escolhas são: Área: ${perguntaUm} | Linguagem: ${perguntaDois} | Desejo: ${perguntaTres} | Novas tecnologias que deseja aprender: ${perguntaQuatro}`;
}

function perguntaArea(){
    let opcaoArea;
    do{
        opcaoArea = prompt("Qual área deseja seguir? Escolha 1-Front-End ou 2-Back-End");
    }while (opcaoArea != '1' && opcaoArea != '2');
    return (opcaoArea == '1') ? "Front-End" : "Back-End";
}

function perguntaLinguagem(pArea){
    let opcaoLinguagem;
    do{
        if (pArea == "Front-End"){
            opcaoLinguagem = prompt("Qual linguagem deseja aprender? Escolha 1-React ou 2-Vue");
        }
        if (pArea == "Back-End"){
            opcaoLinguagem = prompt("Qual linguagem deseja aprender? Escolha 1-C# ou 2-Java");
        }
    }while (opcaoLinguagem != 1 && opcaoLinguagem != 2);
    return (pArea == "Front-End") ? (opcaoLinguagem == 1) ? "React" : "Vue" : (opcaoLinguagem == 1) ? "C#" : "Java";
}

function perguntaDesejo(){
    let opcaoDesejo;
    do{
        opcaoDesejo = prompt(`Você deseja (escolha 1 ou 2): \n1-Seguir se especializando na área escolhida \n2-Seguir se desenvolvendo para se tornar FullStack`);
    }while (opcaoDesejo == 1 && opcaoDesejo == 2);
    return (opcaoDesejo == 1) ? "Seguir se especializando na área escolhida" : "Seguir se desenvolvendo para se tornar FullStack";
}

function perguntaNovasTecnologias(){
    let opcaoNovaTecnologia;
    let arrayNovaTecnologia = [];
    opcaoNovaTecnologia = prompt("Digite uma tecnologias que deseja aprender. Digite 0 para sair.");
    while (opcaoNovaTecnologia != 0) {
       arrayNovaTecnologia.push(opcaoNovaTecnologia);
       opcaoNovaTecnologia = prompt("Digite uma tecnologias que deseja aprender. Digite 0 para sair.");
    }; 
    return arrayNovaTecnologia;
}

perguntasDiaTres.addEventListener('click', fluxoDecisao);