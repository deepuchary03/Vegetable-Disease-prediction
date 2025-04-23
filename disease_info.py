def get_disease_info(disease_name):
    """
    Returns information about the given plant disease.
    
    Args:
        disease_name: The name of the disease class
        
    Returns:
        A dictionary containing description, treatment, and prevention information
    """
    # Dictionary containing information about various plant diseases
    disease_info = {
        'Tomato___Bacterial_spot': {
            'description': 'Bacterial spot is a disease of tomato caused by Xanthomonas bacteria. It causes small, dark, water-soaked, circular spots on leaves, stems, and fruits.',
            'treatment': [
                'Apply copper-based fungicides or bactericides as recommended by your local extension service.',
                'Remove and destroy infected plant debris.',
                'Prune infected parts of the plant.'
            ],
            'prevention': [
                'Use disease-free seeds and transplants.',
                'Practice crop rotation with non-solanaceous crops.',
                'Avoid overhead irrigation; water at the base of plants.',
                'Space plants properly to ensure good air circulation.',
                'Sterilize gardening tools regularly.'
            ]
        },
        'Tomato___Early_blight': {
            'description': 'Early blight is a fungal disease caused by Alternaria solani. It typically appears on older leaves first with dark spots that form concentric rings, creating a target-like pattern.',
            'treatment': [
                'Apply fungicides containing chlorothalonil, mancozeb, or copper.',
                'Remove and destroy infected leaves and plant debris.',
                'Improve air circulation around plants by pruning.'
            ],
            'prevention': [
                'Practice crop rotation with non-solanaceous crops.',
                'Use mulch to prevent soil splash onto leaves.',
                'Water at the base of plants and avoid wetting the foliage.',
                'Ensure adequate plant spacing for good air circulation.',
                'Choose resistant varieties when available.'
            ]
        },
        'Tomato___Late_blight': {
            'description': 'Late blight is a devastating fungal disease caused by Phytophthora infestans. It causes large, dark brown patches on leaves with white fungal growth underneath. It can quickly kill plants and spread rapidly in cool, wet conditions.',
            'treatment': [
                'Apply fungicides containing chlorothalonil, mancozeb, or copper hydroxide.',
                'Remove and destroy infected plants to prevent spread.',
                'Harvest remaining healthy fruits from infected plants.'
            ],
            'prevention': [
                'Plant resistant varieties.',
                'Avoid overhead irrigation.',
                'Ensure good air circulation by proper spacing and pruning.',
                'Remove volunteer tomato and potato plants.',
                'Apply preventative fungicides during cool, wet weather.'
            ]
        },
        'Tomato___Leaf_Mold': {
            'description': 'Tomato leaf mold is a fungal disease caused by Passalora fulva. It appears as yellow spots on the upper sides of leaves and olive-green to grayish-purple fuzzy growth on the undersides. It thrives in high humidity environments.',
            'treatment': [
                'Apply fungicides containing chlorothalonil or copper compounds.',
                'Remove and destroy infected leaves.',
                'Reduce humidity around plants by improving air circulation.'
            ],
            'prevention': [
                'Use resistant varieties when available.',
                'Ensure proper spacing between plants for good air circulation.',
                'Use drip irrigation instead of overhead watering.',
                'Remove lower leaves and suckers to improve air flow.',
                'Maintain good greenhouse ventilation if growing indoors.'
            ]
        },
        'Tomato___Septoria_leaf_spot': {
            'description': 'Septoria leaf spot is a fungal disease caused by Septoria lycopersici. It appears as numerous small, circular spots with dark borders and light gray centers on the leaves, typically starting on lower leaves.',
            'treatment': [
                'Apply fungicides containing chlorothalonil, mancozeb, or copper.',
                'Remove and destroy infected leaves.',
                'Improve air circulation by pruning.'
            ],
            'prevention': [
                'Practice crop rotation with non-solanaceous crops.',
                'Use mulch to prevent soil splash onto leaves.',
                'Water at the base of plants and avoid wetting the foliage.',
                'Remove and destroy all plant debris after harvest.',
                'Avoid working with plants when they are wet.'
            ]
        },
        'Tomato___Spider_mites': {
            'description': 'Spider mites are tiny arachnids that feed on plant cells. Infested leaves have a speckled, yellowish appearance and fine webbing may be visible. Spider mites thrive in hot, dry conditions.',
            'treatment': [
                'Spray plants with water to dislodge mites.',
                'Apply insecticidal soap or neem oil to affected plants.',
                'Use miticides for severe infestations.',
                'Introduce predatory mites for biological control.'
            ],
            'prevention': [
                'Maintain proper humidity around plants; spider mites prefer dry conditions.',
                'Regularly inspect plants for early signs of infestation.',
                'Avoid water stress in plants.',
                'Keep plants well-watered during hot, dry periods.',
                'Avoid excessive nitrogen fertilization.'
            ]
        },
        'Tomato___Target_Spot': {
            'description': 'Target spot is a fungal disease caused by Corynespora cassiicola. It produces brown to black circular lesions with concentric rings that can occur on leaves, stems, and fruits.',
            'treatment': [
                'Apply fungicides containing mancozeb, chlorothalonil, or azoxystrobin.',
                'Remove and destroy infected plant parts.',
                'Improve air circulation by pruning.'
            ],
            'prevention': [
                'Use disease-free seeds and transplants.',
                'Practice crop rotation.',
                'Avoid overhead irrigation.',
                'Space plants properly for good air circulation.',
                'Apply mulch to prevent soil splash onto leaves.'
            ]
        },
        'Tomato___Tomato_Yellow_Leaf_Curl_Virus': {
            'description': 'Tomato Yellow Leaf Curl Virus (TYLCV) is transmitted by whiteflies. Infected plants show upward curling and yellowing of leaves, stunted growth, and significant yield reduction.',
            'treatment': [
                'There is no cure once plants are infected.',
                'Remove and destroy infected plants to prevent spread.',
                'Control whitefly populations with insecticides or insecticidal soaps.',
                'Use reflective mulches to repel whiteflies.'
            ],
            'prevention': [
                'Use resistant varieties.',
                'Use insect screens in greenhouse production.',
                'Apply insecticides to control whitefly populations.',
                'Plant non-host barrier crops around tomato fields.',
                'Avoid planting near other susceptible crops.'
            ]
        },
        'Tomato___Tomato_mosaic_virus': {
            'description': 'Tomato mosaic virus causes mottled light and dark green patterns on leaves, stunted growth, and sometimes fruit deformation. It is mainly spread through mechanical transmission.',
            'treatment': [
                'There is no cure for infected plants; they should be removed and destroyed.',
                'Control aphids that may spread the virus.',
                'Clean tools with a disinfectant before moving between plants.'
            ],
            'prevention': [
                'Use resistant varieties.',
                'Use virus-free seeds and transplants.',
                'Wash hands thoroughly before handling plants.',
                'Sterilize gardening tools with bleach solution or rubbing alcohol.',
                'Control weeds that may harbor the virus.',
                'Avoid using tobacco near tomato plants, as tobacco can carry the virus.'
            ]
        },
        'Tomato___healthy': {
            'description': 'Your tomato plant appears healthy with no visible signs of disease or pest damage.',
            'treatment': [
                'Continue regular maintenance practices.',
                'Monitor plants regularly for any changes.'
            ],
            'prevention': [
                'Water at the base of plants to keep foliage dry.',
                'Provide adequate spacing for good air circulation.',
                'Apply balanced fertilizer as needed.',
                'Remove lower leaves that touch the soil.',
                'Use mulch to prevent soil-borne diseases from splashing onto plants.'
            ]
        },
        'Pepper___Bacterial_spot': {
            'description': 'Bacterial spot in peppers is caused by Xanthomonas bacteria. It appears as small, brown, water-soaked spots on leaves, stems, and fruits that may enlarge and turn dark brown.',
            'treatment': [
                'Apply copper-based bactericides according to label instructions.',
                'Remove and destroy infected plant parts.',
                'Avoid handling plants when wet to prevent spread.'
            ],
            'prevention': [
                'Use disease-free seeds and transplants.',
                'Practice crop rotation with non-solanaceous crops.',
                'Avoid overhead irrigation; water at the base of plants.',
                'Space plants properly to ensure good air circulation.',
                'Sterilize gardening tools regularly.'
            ]
        },
        'Pepper___healthy': {
            'description': 'Your pepper plant appears healthy with no visible signs of disease or pest damage.',
            'treatment': [
                'Continue regular maintenance practices.',
                'Monitor plants regularly for any changes.'
            ],
            'prevention': [
                'Water at the base of plants to keep foliage dry.',
                'Provide adequate spacing for good air circulation.',
                'Apply balanced fertilizer as needed.',
                'Remove weeds that compete for nutrients and can harbor pests.',
                'Use mulch to moderate soil temperature and moisture.'
            ]
        },
        'Potato___Early_blight': {
            'description': 'Early blight in potatoes is caused by the fungus Alternaria solani. It appears as dark brown to black spots with concentric rings, typically on older leaves first.',
            'treatment': [
                'Apply fungicides containing chlorothalonil, mancozeb, or copper.',
                'Remove and destroy infected leaves and plant debris.',
                'Ensure adequate air circulation between plants.'
            ],
            'prevention': [
                'Practice crop rotation with non-solanaceous crops.',
                'Use disease-free seed potatoes.',
                'Hill soil around plants to help prevent spore dispersal.',
                'Water at the base of plants and avoid wetting the foliage.',
                'Ensure proper plant spacing for good air circulation.'
            ]
        },
        'Potato___Late_blight': {
            'description': 'Late blight in potatoes is caused by Phytophthora infestans, the same pathogen that caused the Irish potato famine. It appears as dark, water-soaked spots on leaves that quickly grow into large brown to purplish-black areas.',
            'treatment': [
                'Apply fungicides containing chlorothalonil, mancozeb, or copper hydroxide.',
                'Remove and destroy infected plants to prevent spread.',
                'Harvest remaining healthy tubers if disease is detected.'
            ],
            'prevention': [
                'Plant resistant varieties.',
                'Use certified disease-free seed potatoes.',
                'Avoid overhead irrigation; water at the base of plants.',
                'Ensure good air circulation by proper spacing.',
                'Apply preventative fungicides during cool, wet weather.',
                'Destroy all volunteer potatoes and nightshade weeds.'
            ]
        },
        'Potato___healthy': {
            'description': 'Your potato plant appears healthy with no visible signs of disease or pest damage.',
            'treatment': [
                'Continue regular maintenance practices.',
                'Monitor plants regularly for any changes.'
            ],
            'prevention': [
                'Use certified disease-free seed potatoes.',
                'Practice crop rotation to prevent soil-borne disease buildup.',
                'Water at the base of plants to keep foliage dry.',
                'Hill soil around plants as they grow.',
                'Monitor for Colorado potato beetles and other pests.',
                'Apply balanced fertilizer as needed.'
            ]
        }
    }
    
    # Return information about the disease or None if not found
    return disease_info.get(disease_name, None)
