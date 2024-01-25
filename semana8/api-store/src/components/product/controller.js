import { prisma } from "../../db/index.js";
import { response } from "../../network/responses.js";
import { mapInsertProduct } from "./utils.js";

export async function list(req, res) {
    try {
        const products = await prisma.product.findMany()
        return response({ok:true, res, data:products})
    } catch (error) {
        return response({ok:false, res, data:error.message, status:500})
    }
}

export async function getById(req, res) {
    try {
        const product = await prisma.product.findUnique({
            where: {
                id: Number(req.params.id)
            }
        })
        if (!product) return response({ok:false, res, data:"Product not found", status:500})
        return response({ok:true, res, data:product})
    
    } catch (error) {
        return response({ok:false, res, data:error.message, status:500})
    }
}

export async function store(req, res) {
    try {
        const { ok, data } = mapInsertProduct(req.body)

        if (!ok) {
            return response({ok, res, data, status:500})
        }

        const newProduct = await prisma.product.create({ data })

        return response({ok:true, res, data:newProduct, status:201})
    } catch (error) {
        return response({ok:false, res, data:error.message, status:500})
    } 
}

// export async function update(req, res) {
//     try {
//         const product = await prisma.product.update({
//             where: {
//                 id: Number(req.params.id)
//             },
//             data: req.body
//         })

//         if (!product) return response({ok:false, res, data:"Product not found", status:500})

//         return response({ok:true, res, data:"Product updated"})
//     } catch (error) {
//         return response({ok:true, res, data:error.message})
//     }
// }

// export async function destroy(req, res) {
//     try {
//         await prisma.product.delete({
//             where: {
//                 id: Number(req.params.id)
//             }
//         })
//         return response({ok:true, res, data:"Product deleted"})
//     } catch (error) {
//         return response({ok:true, res, data:error.message})
//     }
// }