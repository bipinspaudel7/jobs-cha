from products.models import ProductVariant
from rest_framework.exceptions import ValidationError

def check_stock_availability(product_variant_id, requested_quantity, existing_quantity=0):
    product_variant = ProductVariant.objects.filter(id=product_variant_id).first()
    
    if not product_variant:
        raise ValidationError(f"Product variant with ID {product_variant_id} does not exist.")

    total_quantity = requested_quantity + existing_quantity
    
    if total_quantity > product_variant.stock:
        raise ValidationError("Variant quantity is out of stock or limit reached for this product variant.")
    
    return product_variant
