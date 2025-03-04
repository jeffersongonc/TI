import { listaCompras, exibirLista } from './diaCinco.js';
const removerDiaSeis = document.getElementById("removerDiaSeis");
let lista = listaCompras;
function remover(event){
    event.preventDefault();
    let categoria = prompt("Digite o nome da categoria do produto que deseja remover:");
    if (categoria.trim() == ""){
        remover(event);
        return;
    }

    let produto = prompt("Digite o nome do produto que deseja remover:");
    if (produto.trim() == ""){
        remover(event);
        return;
    }

    let categoriaExistente = lista.find(item => item[categoria]);
    if (categoriaExistente){
        let indiceCategoria = lista.indexOf(categoriaExistente);
        let indiceProduto = categoriaExistente[categoria].indexOf(produto);
        if (indiceProduto != -1){
            categoriaExistente[categoria].splice(indiceProduto, 1);
            if (categoriaExistente[categoria].length == 0){
                lista.splice(indiceCategoria, 1);
            }
            exibirLista(lista);
        } else {
            alert("Produto não encontrado na categoria.");
        }
    } else {
        alert("Categoria não encontrada.");
    }
}

removerDiaSeis.addEventListener('click', remover);
