INSERT INTO public.annuaire_rdc_entreprise
(
id,
sigle, 
denomination, 
description, 
secteursactivite, 
villescouvertes, 
email, 
telephone, 
adresse, 
siteweb, 
created_at,
updated_at,
photo)
VALUES 

(
gen_random_uuid(),
'IHUSI', 
'IHUSI HOTEL', 
'Service Hotelier de qualite dans la ville de Goma au bord du lac Kivu', 
'Hottelerie/Restauration/Service traiteur', 
'Goma', 
'benjaminbugandwa@gmail.com', 
'0970480293', 
'Goma Grande barriere', 
'www.ihusiservice.org', 
CURRENT_DATE,
CURRENT_DATE,
null);