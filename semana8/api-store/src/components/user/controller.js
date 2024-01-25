import { response } from "../../network/responses.js";
import { prisma } from "../../db/index.js";

export async function list(req, res) {
    try {
        const users = await prisma.user.findMany()
        return response({ok:true, res, data:users})
    } catch (error) {
        return response({ok:false, res, data:error.message, status:500})
    }
}

export async function getById(req, res) {
    try {
        const user = await prisma.user.findUnique({
            where: {
                id: Number(req.params.id)
            }
        })
        if (!user) return response({ok:false, res, data:"User not found", status:500})
        return response({ok:true, res, data:user})
    
    } catch (error) {
        return response({ok:false, res, data:error.message, status:500})
    }
}

export async function store(req, res) {
    try {
        await prisma.user.create({
            data: req.body,
        })

        return response({ok:true, res, data:"User created", status:201})
    } catch (error) {
        return response({ok:false, res, data:error.message, status:500})
    } 
}

export async function update(req, res) {
    try {
        const user = await prisma.user.update({
            where: {
                id: Number(req.params.id)
            },
            data: req.body
        })

        if (!user) return response({ok:false, res, data:"User not found", status:500})

        return response({ok:true, res, data:"User updated"})
    } catch (error) {
        return response({ok:true, res, data:error.message})
    }
}

export async function destroy(req, res) {
    try {
        await prisma.user.delete({
            where: {
                id: Number(req.params.id)
            }
        })
        return response({ok:true, res, data:"User deleted"})
    } catch (error) {
        return response({ok:true, res, data:error.message})
    }
}