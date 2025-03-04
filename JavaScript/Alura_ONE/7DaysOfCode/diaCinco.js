let listaCompras = [];
const perguntasDiaCinco = document.getElementById("perguntasDiaCinco");

function inserirItem(pLista, pCategoria, pProduto){
    let categoriaExistente = pLista.find(item => item[pCategoria]);
    if (categoriaExistente){
        categoriaExistente[pCategoria].push(pProduto);
        categoriaExistente[pCategoria].sort();
    } else{
        let novoItem = {};
        novoItem[pCategoria] = [pProduto];
        pLista.push(novoItem);
        pLista.sort((a, b) => Object.keys(a)[0].localeCompare(Object.keys(b)[0]));
    }
}

function exibirLista(pLista){
    const respostaDiaCinco = document.getElementById("respostaDiaCinco");
    respostaDiaCinco.innerHTML = "";

    pLista.forEach(item => {
        const fCategoria = Object.keys(item)[0];
        const ul = document.createElement("ul");
        ul.textContent = fCategoria;
        item[fCategoria].forEach(produto => {
            const li = document.createElement("li");
            li.textContent = produto;
            ul.appendChild(li);
        });
        respostaDiaCinco.appendChild(ul);
    });
}

function perguntas(event){
    event.preventDefault();
    let adicionar;
    let categoria;
    let produto;

    escolhaIndevida:
    do{
        adicionar = prompt("Deseja adicionar item da lista? (SIM ou NÃO)");
        if (adicionar.toUpperCase() != "SIM" && adicionar.toUpperCase() != "NÃO"){
            continue escolhaIndevida;
        }
        if (adicionar.toUpperCase() == "SIM"){
            dadoInvalido:
            do{
                categoria = prompt("Digite o nome da categoria:");
                produto = prompt("Digite o nome do produto:");
                if (categoria.trim() == "" || produto.trim() == ""){
                    continue dadoInvalido;
                }
                inserirItem(listaCompras, categoria, produto);
            }while (categoria.trim() == "" || produto.trim() == "");
        }

    }while (adicionar.toUpperCase() != "NÃO");
    exibirLista(listaCompras);
}

perguntasDiaCinco.addEventListener('click', perguntas);
export { listaCompras, exibirLista };