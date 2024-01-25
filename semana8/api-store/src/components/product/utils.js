import { output } from "../../util/utils.js"

function mapProduct(product) {
    const productMap = {
        ...product,
        isNew: product.is_new,
        percentageDiscount: product.percentage_discount,
    }

    delete productMap.is_new
    delete productMap.percentage_discount

    if (product.category_id) {
        productMap.categoryId = product.category_id
        delete productMap.category_id
    }

    return productMap
}

export function mapInsertProduct(body) {
    const { product, category } = body

    if (product.category_id && category) {
        return output(false, "No puedes enviar un category_id y category")
    }

    if (product && category) {
        const insertData = {
            ...mapProduct(product),
            category: {
                create: {
                    ...category
                }
            }
        }

        return output(true, insertData)
    }

    return output(true, mapProduct(product))
}