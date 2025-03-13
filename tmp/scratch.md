# POST
curl -X POST -H "Content-Type: application/json" -d '{"product_id": "321", "height": 10, "width": 20, "depth": 30, "weight": 40, "special_handling_instructions": "Fragile"}' http://localhost:8000/packages

curl -X POST -H "Content-Type: application/json" -d '{"product_id": "999", "height": 10, "width": 20, "depth": 30, "weight": 40, "special_handling_instructions": "Fragile"}' http://localhost:8000/packages



# UPDATE
curl -X PUT -H "Content-Type: application/json" -d '{"height": 15, "width": 25, "depth": 35, "special_handling_instructions": "Handle with extreme care"}' http://localhost:8000/packages/15 


# DELETE
curl -X DELETE http://localhost:8000/packages/15