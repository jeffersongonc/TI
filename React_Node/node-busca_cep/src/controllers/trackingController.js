import Correios from "node-correios/lib/correios";

let correios = new Correios();

class trackingController{
    async index(req, res){
        const {tracking} = req.query;
        correios.consultaCEP({cep: tracking})
        .then(result => {
            res.json(result);
            //console.log(result);
            
        })
        .catch(error => {
            if (res.status(400)){
                return res.status(400).json({ error: "CEP informado é inválido."});
            }
            if (res.status(404)){
                return res.status(404).json({ error: "Página não encontrada."});
            }
            if (res.status(500)){
                return res.status(500).json({ error: "Erro interno do servidor."});
            }
        });
    }
    }
    export default new trackingController();