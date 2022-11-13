class helloController{
    async index(req, res){
        return res.json({hello: 'world'});
    }
    }
    export default new helloController();