// Ahora se debe crear un servidor que se ejecute en un puerto
// de la computadora

/* Los puertos recomendados son:
- 3000
- 6000
- 9000
*/

// Formas de usar express:
// Forma antigua
// const express = require("express")

// Forma moderna
import express from "express";
import { apiVersion } from "./config/index.js";
import { userRouter, productRouter } from "./components/index.js";

export const app = express();

app.use(express.json());

app.use(`${apiVersion}/users`, userRouter);
app.use(`${apiVersion}/products`, productRouter);