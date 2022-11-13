import { Router } from "express";
import { route } from "express/lib/router";
import helloController from "./controllers/helloController";
import trackingController from "./controllers/trackingController";

const routes = new Router();

routes.get('/hello', helloController.index);

routes.get('/tracking', trackingController.index);

export default routes;