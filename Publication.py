class CarPublication():
    def __init__(self):
        self.id = None
        self.category_id = None
        self.title = None
        self.condition = None
        self.car_year = None
        self.brand = None
        self.model = None
        self.version = None
        self.engine = None
        self.engine_power = None
        self.doors = None        
        self.km = None
        self.fuel_type = None        
        self.traction_control = None
        self.passenger_capacity = None
        self.transmission = None
        self.currency = None
        self.price = None
        self.seller_id = None
        self.seller_nickname = None
        self.is_car_shop = None
        self.seller_country = None
        self.seller_state = None
        self.seller_city = None
        self.seller_neighborhood = None


class CarPublicationBuilder():
    def __init__(self, data:dict):
        self.data = data
        self.publication = CarPublication()

    def build(self):
        self.publication.id = self._get_id()
        self.publication.category_id = self._get_category_id()
        self.publication.title = self._get_title()
        self.publication.condition = self._get_condition()
        self.publication.car_year = self._get_car_year()
        self.publication.brand = self._get_brand()
        self.publication.model = self._get_model()
        self.publication.version = self._get_version()
        self.publication.engine = self._get_engine()
        self.publication.engine_power = self._get_engine_power()
        self.publication.doors = self._get_doors()
        self.publication.km = self._get_km()
        self.publication.fuel_type = self._get_fuel_type()     
        self.publication.traction_control = self._get_traction_control()
        self.publication.passenger_capacity = self._get_passenger_capacity()
        self.publication.transmission = self._get_transmission()
        self.publication.currency = self._get_currency()
        self.publication.price = self._get_price()
        self.publication.seller_id = self._get_seller_id()
        self.publication.seller_nickname = self._get_seller_nickname()
        self.publication.is_car_shop = self._get_is_oficial_store()
        self.publication.seller_country = self._get_seller_country()
        self.publication.seller_state = self._get_seller_state()
        self.publication.seller_city = self._get_seller_city()
        self.publication.seller_neighborhood = self._get_seller_neighborhood()
        return vars(self.publication)

    def _get_id(self):
        return self.data.get('id', None)
    
    def _get_category_id(self):
        return self.data.get('category_id', None)
    
    def _get_title(self):
        return self.data.get('title', None)
    
    def _get_condition(self):
        for item in self.data['attributes']:
            if ('id' in item) and (item['id'] == 'ITEM_CONDITION'):
                return item['value_name']
        return None
    
    def _get_car_year(self):
        for item in self.data['attributes']:
            if ('id' in item) and (item['id'] == 'VEHICLE_YEAR'):
                return item['value_name']
        return None
    
    def _get_brand(self):
        for item in self.data['attributes']:
            if ('id' in item) and (item['id'] == 'BRAND'):
                return item['value_name']
        return None
    
    def _get_model(self):
        for item in self.data['attributes']:
            if ('id' in item) and (item['id'] == 'MODEL'):
                return item['value_name']
        return None
    
    def _get_version(self):
        for item in self.data['attributes']:
            if ('id' in item) and (item['id'] == 'TRIM'):
                return item['value_name']
        return None
    
    def _get_engine(self):
        for item in self.data['attributes']:
            if ('id' in item) and (item['id'] == 'ENGINE'):
                return item['value_name']
        return None
    
    def _get_engine_power(self):
        for item in self.data['attributes']:
            if ('id' in item) and (item['id'] == 'POWER'):
                return item['value_name']
        return None
    
    def _get_doors(self):
        for item in self.data['attributes']:
            if ('id' in item) and (item['id'] == 'DOORS'):
                return item['value_name']
        return None
    
    def _get_km(self):
        for item in self.data['attributes']:
            if ('id' in item) and (item['id'] == 'KILOMETERS'):
                return item['value_name']
        return None
    
    def _get_fuel_type(self):
        for item in self.data['attributes']:
            if ('id' in item) and (item['id'] == 'FUEL_TYPE'):
                return item['value_name']
        return None
    
    def _get_traction_control(self):
        for item in self.data['attributes']:
            if ('id' in item) and (item['id'] == 'TRACTION_CONTROL'):
                return item['value_name']
        return None
    
    def _get_passenger_capacity(self):
        for item in self.data['attributes']:
            if ('id' in item) and (item['id'] == 'PASSENGER_CAPACITY'):
                return item['value_name']
        return None
    
    def _get_transmission(self):
        for item in self.data['attributes']:
            if ('id' in item) and (item['id'] == 'TRANSMISSION'):
                return item['value_name']
        return None
    
    def _get_currency(self):
        return self.data.get('currency_id', None)
    
    def _get_price(self):
        return self.data.get('price', None)
    
    def _get_seller_id(self):
        return self.data.get('seller', {}).get('id', None)
    
    def _get_seller_nickname(self):
        return self.data.get('seller', {}).get('nickname', None)
    
    def _get_is_oficial_store(self):
        return self.data.get('official_store_id', None) is not None
    
    def _get_seller_country(self):
        return self.data.get('location',{}).get('country', {}).get('name', None)
    
    def _get_seller_state(self):
        return self.data.get('location',{}).get('state', {}).get('name', None)
    
    def _get_seller_city(self):
        return self.data.get('location',{}).get('city', {}).get('name', None)
    
    def _get_seller_neighborhood(self):
        return self.data.get('location',{}).get('neighborhood', {}).get('name', None)