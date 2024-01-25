export function response({ok=true, res, data, status=200}) {
    return res.status(status).json({
        ok,
        data,
    })
}