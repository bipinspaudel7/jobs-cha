from products.models import ProductVariant
from rest_framework.exceptions import ValidationError

def validate_order_quantity(product_variant_id, requested_quantity, existing_quantity=0):
    product_variant = ProductVariant.objects.filter(id=product_variant_id).first()
    
    if not product_variant:
        raise ValidationError(f"Product variant with ID {product_variant_id} does not exist.")

    min_order_quantity = product_variant.product.minimum_order_quantity
    max_order_quantity = product_variant.product.maximum_order_quantity

    total_quantity = requested_quantity + existing_quantity

    if requested_quantity < min_order_quantity:
        raise ValidationError(f"Quantity must be at least {min_order_quantity}.")
    
    if total_quantity > max_order_quantity:
        raise ValidationError(f"Cannot exceed maximum order quantity of {max_order_quantity} for this product variant.")

    return product_variant
