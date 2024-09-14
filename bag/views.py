from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages

from products.models import Product

# Create your views here.

def view_bag(request):
    '''
    A view to return the bag contents page
    '''
    return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    # check the user’s session to see if there’s already a shopping bag stored.
    bag = request.session.get('bag', {})

    # Check if the product (item_id) is already in the shopping bag.
    if item_id in list(bag.keys()):
        # If the product is already in the bag increment the quantity of that product 
        bag[item_id] += quantity
    else:
        # If the product is not in the bag add it with the specified quantity
        bag[item_id] = quantity
        # Display success message to the user
        messages.error(request, f'Added {product.name} to your bag')

    # Save the shopping bag into the user's session
    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """ Adjust quantuty of an item to a specfied amount """

    product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        # Update the quantity of the item in the bag
        bag[item_id] = quantity
    else:
        # Remove the item from the bag if quantity is 0 or less
        bag.pop(item_id)

    # Save the updated bag back to the session
    request.session['bag'] = bag
    return redirect(reverse('view_bag'))

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """ Remove the item from the shopping bag """

    try:
        bag = request.session.get('bag', {})

        # Remove the item from the bag
        if item_id in bag:
            bag.pop(item_id)

        # Save the updated bag back to the session
        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)