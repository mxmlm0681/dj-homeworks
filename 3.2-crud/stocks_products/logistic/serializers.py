from rest_framework import serializers

from logistic.models import Product, Stock, StockProduct


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description']


class ProductPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockProduct
        fields = ['id', 'stock', 'product']


class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)

    class Meta:
        model = Stock
        fields = ['id', 'name', 'description', 'positions']

    def create(self, validated_data):
        positions = validated_data.pop('positions')
        stock = super().create(validated_data)
        for pos in positions:
            stockProduct = StockProduct(quantity=pos['quantity'],
                                         price=pos['price'],
                                         product=pos['product'],
                                         stock=stock)
            stock_product.save()
            return stock



    def update(self, instance, validated_data):
        positions = validated_data.pop('positions')
        stock = super().update(instance, validated_data)
        stock.positions.filter(stock_id=stock.id).delete()
        for pos in positions:
            StockProduct.objects.update_or_create(stock=stock, **pos)
        return stock

