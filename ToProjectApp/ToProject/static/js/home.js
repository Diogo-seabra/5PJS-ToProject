
function carregaPropostas(){


}

function getCSRFToken() {
    return document.querySelector('[name=csrf-token]').content;
}

//pouplar as proposta com passando o id ao chamar do banco 
function selecionaProposta(Proposta){

    // alert("teste de clique card") 
    console.log(Proposta)
}
// ao selecionar uma proposta ele leva para outra pagina com a proposta carregada

function confirmDelete(Proposta_id) {
    if (confirm("Tem certeza de que deseja excluir esta proposta?")) {
        deleteRegistro(Proposta_id);
    }
}

function deleteRegistro(registroId) {

    const csrftoken = getCSRFToken()
    fetch(`/deletar_registro/${registroId}/`, {
        method: 'DELETE',
        headers: {
            'X-CSRFToken': csrftoken  // Inclui o token CSRF para segurança
        }
    })
    .then(response => {
        if (response.ok) {
            document.getElementById(`card-${registroId}`).remove();  // Remove o card do DOM
            alert("Proposta excluída com sucesso!");
        } else {
            alert("Erro ao excluir a proposta.");
        }
    })
    .catch(error => {
        console.error("Erro:", error);
        alert("Erro ao excluir a proposta.");
    });
}